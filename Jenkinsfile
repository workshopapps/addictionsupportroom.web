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
                            sh "sudo cp -fr ${WORKSPACE}/frontend/build/* /var/www/soberpal.hng.tech/html"
//                           sh "sudo su - judgejudy && whoami"
//                           sh "sudo systemctl restart addictionsupportroom.service"
			    sh "sudo bash /home/judgejudy/addictionsupportroom.sh"
                    }

        }
		
	stage("remove files") {
			
		steps {
			     sh "sudo rm -rf *"
			}
		}


        }


}
