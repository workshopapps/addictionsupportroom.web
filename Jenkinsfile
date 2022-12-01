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
                            sh "sudo cp -rf backend /home/judgejudy/addictionsupportroom.web/backend"
                            sh "sudo cp -fr ${WORKSPACE}/frontend/build/* /home/judgejudy/addictionsupportroom.web/frontend"
                            sh "sudo su - judgejudy && whoami"
                            sh "sudo pm2 stop soberpal"
	    		    sh "sudo pm2 stop server"
                            sh "sudo pm2 serve /home/judgejudy/frontend/build --port 3344"
                            sh "sudo pm2 start /home/judgejudy/backend/app/server.py --interpreter python3"
                    }

        }


        }


}
