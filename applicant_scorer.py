import predictor
from person import Person
from jsonconstants import JSONConstants


class Scorer:
    def score_people(self, people, predictor_impl: predictor.Predictor, people_name: str):
        scores = []
        for person in people:
            score = {JSONConstants.name: person[JSONConstants.name], JSONConstants.score: (
                predictor_impl.predict(Person(person)))}
            scores.append(score)
        scored_applicants = {people_name: scores}
        return scored_applicants

    def process_file(self, teams_and_applicants, people_type: str, label: str, predictor_impl: predictor.Predictor):
        return self.score_people(teams_and_applicants[people_type], predictor_impl, label)

