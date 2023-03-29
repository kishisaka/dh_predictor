import json

import applicant_scorer
from dh_predictor import Predictor
from jsonconstants import JSONConstants


def print_scores():
    scorer = applicant_scorer.Scorer()
    predictor = Predictor()
    json_file = json.load(open("data.json"))
    print(json.dumps(
        scorer.process_file(json_file, JSONConstants.applicants, "scoredApplicants", predictor), indent=4)
    )

print_scores()
