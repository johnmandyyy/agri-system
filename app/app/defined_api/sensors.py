from rest_framework.views import APIView
from app.defined_api.decision_tree import Tree
from rest_framework.response import Response

class TrainData(APIView):
    """ An API to train dataset(s). """

    def __init__(self):
        """ A constructor for datasets """
        pass

    def get(self, request):
        """ Executes when POST is executed. """
        tree_instance = Tree()
        tree_instance.decisionTree()

        return Response({
            "message": "Training is done.",
        }, 200)
    

class Sensor(APIView):
    """ An API View for sensor(s). """

    def __init__(self):
        """ A constructor for Sensor """
        pass

    def post(self, request):
        """ Executes when POST is executed. """

        anemometer = request.data.get('anemometer', 0)
        rainfall = request.data.get('rainfall', 0)
        humidity = request.data.get('humidity', 0)

        message = 'No storm.'

        tree_instance = Tree()
        prediction = tree_instance.predictAlgorithm({
            "anemometer": anemometer,
            "rainfall": rainfall,
            "humidity": humidity
        })

        if prediction[0] == True:
            message = 'A storm might occur.'

        return Response({'message': message}, 200)
        


        

        