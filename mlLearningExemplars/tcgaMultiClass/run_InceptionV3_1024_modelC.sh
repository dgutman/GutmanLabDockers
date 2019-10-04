
nvidia-docker run \
     -it --rm -p222:8888 \
     -v "${PWD}:/app:rw" \
     -v "/home/dagutman/devel/tcga_multiclass_classifier_CNN/code:/data/code:rw" \
     -v "/home/dagutman/devel/tcga_multiclass_classifier_CNN/results:/data/output/results:rw" \
     -v "/home/dagutman/data/10k_tiles_data/train:/data/train:rw" \
     -v "/home/dagutman/data/10k_tiles_data/test:/data/test:rw" \
     --entrypoint bash \
     fgiuste/neuroml:V3
