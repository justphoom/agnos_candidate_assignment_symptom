# symptom-assignment

To describe the solution of this problem, there are 2 parts for the solution.
Basically, the solution contains the prediction algorithm part, and the user-interface part.

First, the user-interface part. The solution was developed with Streamlit library to handle the form. It designed to get the values from patient, then send to the calculation for prediction as a result.

Second, to predict the additional symptoms, this requires a language model to calculate. The solution is to consider each data as a vector, when the new data is put for a prediction, it will calculate the nearest angle to see the most possible disease. Then collect other near solution, to gain some options as a possible symptom chice.

In addition, the result and screenshots are attached below.

This is the like for a playable prototype: https://agnoscandidateassignmentsymptom-4qvey6kzdisveh7vapftxe.streamlit.app/

/example1.png
/example2.png
