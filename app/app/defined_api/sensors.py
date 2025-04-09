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

    def universal_mapping(self, value, old_min=0, old_max=100, new_min=0, new_max=999):
        """ Map a value from one range to another. """

        if old_max - old_min == 0:
            return 0

        mapped_value = ((value - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min
        return int(mapped_value)  # return as integer

    def post(self, request):
        """ Executes when POST is executed. """

        anemometer = request.data.get('anemometer', 0)
        rainfall = request.data.get('rainfall', 0)
        humidity = request.data.get('humidity', 0)

        humidity = self.universal_mapping(humidity, old_min=0, old_max=100, new_min=0, new_max=999)
        rainfall = self.universal_mapping(rainfall, old_min=0, old_max=100, new_min=0, new_max=999)
        anemometer = self.universal_mapping(anemometer, old_min=0, old_max=100, new_min=0, new_max=999)
        
        print(humidity, "Mapped Humidity")
        print(rainfall, "Mapped Rainfall")
        print(anemometer, "Mapped Anemometer")

        message = 'No storm.'
        remark = 0

        tree_instance = Tree()
        prediction = tree_instance.predictAlgorithm({
            "anemometer": anemometer,
            "rainfall": rainfall,
            "humidity": humidity
        })

        if prediction[0] == True:
            message = 'A storm might occur.'
            remark = 1

        return Response({'message': message, 'remark': remark}, 200)
        


        

        