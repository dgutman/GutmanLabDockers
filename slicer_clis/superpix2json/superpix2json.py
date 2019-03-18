import json
import numpy as np
import cv2

import iputils as ip
from ctk_cli import CLIArgumentParser

import logging
logging.basicConfig(level=logging.CRITICAL)


def TileMap_to_SVG(input_image_file, output_json_file, debug=False):
    """
    This function takes an input image as a PNG File and produces a pointlist of the
    outer most contour for each label map, and produces a format I can read in as SVG for visualization"""
    # Load an color image in grayscale; currently not working with > 256 superpixels
    img = cv2.imread(input_image_file)

    img_ch0 = img[:,:,0]
    img_ch1 = img[:,:,1]
    img_ch2 = img[:,:,2]
    
    img_minor = img_ch2  ## Need to double check this
    img_major = img_ch1   ## Also check this

    img_gray = 256 * img_major.astype(np.int) + img_minor.astype(np.int) +1 ##Allows > 256 Channels
    ### Probably should add a 1 to get rid of the 0th channel.. this is a TO DO
    
    unique_labels = np.unique(img_gray)
    if debug: 
        print len(unique_labels)
    
    all_cnts = []
    cntdict = {}
    return_data = []
    ## So a given label/contour can contain one or more features...
    
    ## Now iterate through each label, mask the input image with the label, and find appropriate contours
    for label in unique_labels:
        working_img = img_gray.copy()
        working_img[working_img != label] = 0
        ### this breaks when label == 0
        
        ## can pass cv2.RETR_CCCOMP or RETR_EXTERNAL
        _,contours, hierarchy = cv2.findContours(working_img.astype(np.uint8), 
                                                 cv2.RETR_EXTERNAL, 
                                                 cv2.CHAIN_APPROX_SIMPLE) ## can also do CHAIN_APPROX_TC89_L1
        
        if len(contours) > 0:
            if debug: print "Found %d contours for label %s" % ( len(contours), label)
            for c in contours:    
                try:
                    outerpoly = ip.contourToSVGString( np.squeeze( c ) )            
                    all_cnts.append( { 'geometry': { 'type': 'polygon', 'coordinates': outerpoly }, 'properties' : { 'labelindex': str(label-1)    } } )
                except:
                    print "SOMETHING WRONG IN THIS IMAGE CONTOUR... 2 few points??",c
        else:
            if debug: print len(contours),"were found for label",label
    for c in all_cnts:
        return_data.append(c)
          
    superpixel_contours = return_data
    
    if not os.path.isfile(output_json_file):
        with  open(svg_output_file,'w') as outfile:
            json.dump(superpixel_contours, outfile)


def main(args):
    TileMap_to_SVG(args.in_file, args.out_file)
    

if __name__ == "__main__":
    main(CLIArgumentParser().parse_args())
    
