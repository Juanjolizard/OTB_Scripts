import processing
import os

src_file = 'C:/datos_otb/RoadExtract.tif'

dst_folder = 'C:/otb_output'
if not os.path.exists(dst_folder):
    os.mkdir(dst_folder)
else:
    print("folder already exists....")

operations = ["dilate", "erode", "opening", "closing"] 

if operations:
    for operation in operations:
        dst_name = os.path.splitext(os.path.basename(src_file))[0]
        #print(dst_name)
        try:
            parameters = { 'in': src_file,
            'out': os.path.join(dst_folder, dst_name + '_' + operation + '.tif'),
            'channel': 1,
            'structype': 'cross',
            'xradius': 5,
            'yradius': 5,
            'filter': operation,
            'outputpixeltype': 1}
            feedback = QgsProcessingFeedback()
            processing.runAndLoadResults('otb:GrayScaleMorphologicalOperation', parameters, feedback=feedback)
            print("generating images.....")
        except:
            print("error during processing")