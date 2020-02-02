# Project1
Continuous Delivery of Flask Application on GCP 

1. Create Project
2. Activate cloud shell
3. Refer to hello world docs for python3 app engine: https://cloud.google.com/appengine/docs/standard/python3/quickstart
4. Run describe
   verify project is working :
   
   gcloud projects describe $GOOGLE_CLOUD_PROJECT
   
   output should look similar to this:
createTime: '2019-05-29T21:21:10.187Z'
lifecycleState: ACTIVE
name: helloml
projectId: helloml-xxxxx
projectNumber: '881692383648'

5. You may want to verify you have the correct project and if not, do this to switch:
   
   gcloud config set project $GOOGLE_CLOUD_PROJECT
   
6. Create app engine app:
 
   gcloud app create
   
   this will ask for the region. Go ahead and pick us-central [12]
   
7. Clone the hello world sample app repo:
    
    git clone https://github.com/GoogleCloudPlatform/python-docs-samples
    
8. cd into the repo:
   
   cd python-docs-samples/appengine/standard_python37/hello_world

9. Update Cloudshell image [NOTE this is optional....you don't need this]

  
git clone https://github.com/noahgift/gcp-hello-ml.git
Update .cloudshellcustomimagerepo.json with project and image name
TIP: enable "Boost Mode" in in Cloudshell

        cloudshell env build-local
        cloudshell env push
        cloudshell env update-default-image


Restart Cloudshell VM

10. create and source the virtual environment:

   virtualenv --python $(which python3) venv
   source venv/bin/activate
# Make sure you have the latest python 

11. activate cloud shell editor

12. run flask locally
   
   python main.py
   
13. Preview the results using web preview at the right side corner of cloud shell editor using port 8080.

14.  update main.py by adding different approute (optional)

15. Now deploy the App
    
    gcloud app deploy
    
16. Now stream the log files:
    
    gcloud app logs tail -s default

