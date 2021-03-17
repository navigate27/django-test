from django.shortcuts import render
import requests


# Create your views here.
def invest(request):
    apikey = 'yNFqIYsS5_stJgbsUVhg3MUISuEff9Au'
    response = requests.get('https://sandbox.fundamerica.com/api/offerings', auth=(apikey, ''))
    print(response.text)
    return render(request, 'investform/result.html')


def test(request):
    # POST
    # data = {
    #     'name': 'OBJECT NAME'
    # }
    #
    # response = requests.post('https://apps.fundamerica.com/api/example_objects', data=data,
    #                          auth=('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', ''))

    # GET
    # response = requests.get('https://apps.fundamerica.com/api/example_objects/XXXXXXXXXXXXXXXXXXXXXX',
    #                         auth=('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', ''))

    # PATCH
    # data = {
    #     'name': 'OBJECT NEW NAME'
    # }
    #
    # response = requests.patch('https://apps.fundamerica.com/api/example_objects/XXXXXXXXXXXXXXXXXXXXXX', data=data,
    #                           auth=('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', ''))

    # DELETE
    # response = requests.delete('https://apps.fundamerica.com/api/example_objects/XXXXXXXXXXXXXXXXXXXXXX',
    #                            auth=('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', ''))


    apikey = 'yNFqIYsS5_stJgbsUVhg3MUISuEff9Au'

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        # "custodian_entity_id" : "1324132",
        # "other_entity_ids" : "1324132",
        "primary_entity_id" : "m9T78jvkS3-IXzD6w7b3ww",
        "type" : "company",
    }

    response = requests.get('https://sandbox.fundamerica.com/api/entities', auth=(apikey, ''))

    print(response.text)
    return render(request, 'investform/result.html')
