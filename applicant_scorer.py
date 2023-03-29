import json

import dh_predictor
from person import Person
from jsonconstants import JSONConstants


class Scorer:
    def score_people(self, teams_and_applicants, predictor: dh_predictor.Predictor, people_name: str):
        scores = []
        for applicant in teams_and_applicants:
            score = {JSONConstants.name: applicant[JSONConstants.name], JSONConstants.score: (
                predictor.predict(Person(applicant)))}
            scores.append(score)
        scored_applicants = {people_name: scores}
        return scored_applicants

    def process_file(self, file: str, people_type: str, label: str, predictor: dh_predictor.Predictor):
        json_file = open(file)
        teams_and_applicants = json.load(json_file)
        return self.score_people(teams_and_applicants[people_type], predictor, label)

