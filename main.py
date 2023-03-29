import json

import applicant_scorer
from dh_predictor import Predictor
from jsonconstants import JSONConstants


def print_scores():
    scorer = applicant_scorer.Scorer()
    predictor = Predictor()
    print(json.dumps(
        scorer.process_file("data.json", JSONConstants.applicants, "scoredApplicants", predictor), indent=4)
    )

print_scores()
