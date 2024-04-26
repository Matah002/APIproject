from django.shortcuts import render
import requests

def home(request):
  response = requests.get('https://api.github.com/events')
  data = response.json()
  result = data[0]["id"]

  response2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = response2.json()
  result2 = data2["message"]

  response3 = requests.get('https://api.thecatapi.com/v1/images/search')
  data3 = response3.json()
  result3 = data3[0]["url"]

  response4 = requests.get('https://api.thedogapi.com/v1/images/search')
  data4 =response4.json()
  result4 =data4[0]["url"]

  response5 = requests.get('https://www.boredapi.com/api/activity')
  data5 = response5.json()
  result5 = data5['activity']

  response6 = requests.get('https://api.chucknorris.io/jokes/random')
  data6 = response6.json()
  result6 = data6['value']

  
                          
  return render(request,
                'templates/index.html',
                {
                  'result': result,
                  'result2':result2, 
                  'result3':result3, 
                  'result4':result4, 
                  'result5':result5, 
                  'result6':result6
                }
               )


