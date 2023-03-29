import dh_predictor
from person import Person
from jsonconstants import JSONConstants


class Scorer:
    def score_people(self, people, predictor: dh_predictor.Predictor, people_name: str):
        scores = []
        for person in people:
            score = {JSONConstants.name: person[JSONConstants.name], JSONConstants.score: (
                predictor.predict(Person(person)))}
            scores.append(score)
        scored_applicants = {people_name: scores}
        return scored_applicants

    def process_file(self, teams_and_applicants, people_type: str, label: str, predictor: dh_predictor.Predictor):
        return self.score_people(teams_and_applicants[people_type], predictor, label)

