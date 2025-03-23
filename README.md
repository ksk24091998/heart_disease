# heart_disease
1.first created a repo 							
2.copied the link of repo							
3.opened command prompt							cd ../../
4.gave the foler path to where I need to add the data							
5.git clone "repo link"							cd ./src/
6.opened vscode							
7.create new environment							
conda create -p venv python==3.8 -y							
8.create artifacts folder - put the data inside it							
9.created data ingestion notebook inside src/components							
10.created requirements.txt file and tried using  pip install -r requirements.txt							
11.created data transformation notebook							
12.created model_trainer.py							
13.create html page							
14.create predict_pipeline							
15.create templates/home.html							
16.create app.py							
17.link app.py , home.html ,predict_pipeline							
18.create logger and exception files							
19.Create docker file and changed the path to docker app path in predict_pipeline..if u want to run app.py,change the path
20.docker build -t {name} .
21.docker run -p 5000:5000 {name}


git 
1.git add .
2.git commit -m "message"
3.git push origin main