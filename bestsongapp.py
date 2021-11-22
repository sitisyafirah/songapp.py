import streamlit as st 
import pickle

# load the saved model 
pickle_in = open("fordeploy.pkl","rb")
model=pickle.load(pickle_in)

result=predict_popu(acousticness,danceability,duration_ms,energy,loudness,speechiness,valence)
def predict_popu(acousticness,danceability,duration_ms,energy,loudness,speechiness,valence):
    """
    this method is for prediction process 
    takes all the Audio characteristics thtat we used for modelling and returns the prediction 
    """
    prediction=model.predict([[acousticness,danceability,duration_ms,energy,loudness,speechiness,valence]])
    print(prediction)
    return prediction

def main():
    st.title("Spotify songs")
    st.write("Disclaimer: This app does for learning purpose only.")
    acousticness = st.text_input("acousticness","Type Here")
    danceability = st.text_input("danceability","Type Here")
    duration_ms = st.text_input("duration_ms","Type Here")
    energy = st.text_input("energy","Type Here")
    loudness = st.text_input("loudness","Type Here")
    speechiness = st.text_input("speechiness","Type Here")
    valence = st.text_input("valence","Type Here")
    result=""

    if st.button("Predict"):
    #result=predict_popu(acousticness,danceability,duration_ms,energy,loudness,speechiness,valence)
        st.write('The score is {}'.format(result))
    # one more button saying About ...
    
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
