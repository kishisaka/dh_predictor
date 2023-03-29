import predictor
from person import Person


class DatahousePredictor(predictor.Predictor):

    def predict(self, applicant: Person):
        return (applicant.attributes.endurance +
                applicant.attributes.strength +
                applicant.attributes.intelligence +
                applicant.attributes.spicyFoodTolerance) / 100
