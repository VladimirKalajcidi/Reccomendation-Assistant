import argparse
from recommendationAssistant.inference import PredictionPipeline
 
parser = argparse.ArgumentParser(description="main")
parser.add_argument("-i", "--input", help="input text", required=True)
args = parser.parse_args()


pipe = PredictionPipeline(args.input)
output = pipe.generate()

with open('output.txt', 'w') as f:
    f.write(output)

