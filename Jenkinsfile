pipeline {

    	agent any
	    stages {
		
		

		            stage("build frontend"){

                      steps {
                              sh "cd frontend"
                              sh "cd frontend && npm i --force && CI=false npm run build"
                	    } 
        }
        stage("build backend"){

                      steps {
                              sh "cd backend"
                              sh "cd backend && python3 -m pip install --upgrade pip"
                              sh "cd backend/app && pip install -r requirements.txt"
                	} 
        }
            stage("deploy") {

                    steps {
			    sh "sudo cp -rf ${workspace}/backend/app/* /home/judgejudy/addictionsupportroom/backend"
                            sh "sudo cp -fr ${WORKSPACE}/frontend/* /home/judgejudy/addictionsupportroom/frontend"
                            sh "sudo su - judgejudy && whoami"
                            sh "sudo pm2 stop soberpal"
			    sh "sudo pm2 stop server"
                            sh "sudo pm2 serve /home/judgejudy/addictionsupportroom/frontend/build --port 3344 --name soberpal"
                            sh "sudo pm2 start /home/judgejudy/addictionsupportroom/backend/server.py --interpreter python3"
                    }

        }


        }


}
