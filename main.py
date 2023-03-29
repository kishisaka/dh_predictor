import json

import applicant_scorer
from datahouse_predictor import DatahousePredictor
from jsonconstants import JSONConstants


def print_scores():
    scorer = applicant_scorer.Scorer()
    predictor = DatahousePredictor()
    json_file = json.load(open("data.json"))
    print(json.dumps(
        scorer.process_file(json_file, JSONConstants.applicants, "scoredApplicants", predictor), indent=4)
    )

print_scores()
