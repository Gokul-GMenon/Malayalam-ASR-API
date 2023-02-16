# Malayalam-ASR-API
This is an API we built for a Malayalam Automatic Speech Recognition model done as part of the ICISCoIS 2023 conference.

- The API has been done on django. The model used can be cloned from our repo [here] (https://huggingface.co/5p33ch3xpr/XLS-R-with-LM)
- The API will take an audio file (binary) as input through a post request.
- It will then use the XLS-R with KenLM model finetuned for the Malayalam language (WER: 30% on Non-OOD datasets) to generate the transcript.
- This transcript is then with a Malayalam-English language translator to generate the English transcript (Translator API used can be found [here](https://rapidapi.com/sibaridev/api/rapid-translate-multi-traduction)).
- Gtts is then used to obtain the Audio file for the English translation.
- How to Use
  1.  Clone the Repo
  2.  Install all the dependencies
  3.  Clone the repo of the model from hugging face.
  4.  Host the model somewhere and setup the server.
  4.  Run a post request
