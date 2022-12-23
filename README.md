# Cisco-ITL-Reset
Reset ITL Security files on Cisco IP Phones. This Python program interacts with the IP phone's firmware through its built-in XML objects. The request is processed by the phone's inbuilt HTTP server. This program is specific to Cisco IP Phone model 7841 but the same concept can be used for other phone models by slightly tweaking the payload configuration.

## Prerequisites
- Python 3.x
- Cisco IP Phone 7841 model
- A user profile in CUCM that can control the phone. In other words, the phone should be added to the user's controlled devices list.
- Libraries like Requests

## Cloning the App
You can simply issue the following command from the command prompt on your computer to clone this app to your local directory
```
git clone https://github.com/simranjit-uc/Cisco-ITL-Reset
```
## Running the App
- You can run the app directly from the command prompt or any other program like PyCharm which is what I use.
- Make sure that there is IP connectivity between the IP phone and the machine from where you are running this program.
- Make sure that the phone which needs to be actioned is added to the user's "Controlled Devices" list.

## More details
For more details on what this code means, you can check out the following link

To gain more behind the scene understanding of IP Phone services and how it works the phone's firmware, you can check out the following links

- https://learnuccollab.com/2022/12/04/building-cisco-ip-phone-services-part-1-the-basics/
- https://learnuccollab.com/2022/12/18/building-cisco-ip-phone-services-part-2-the-payload/
