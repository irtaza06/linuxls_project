pipeline {
    agent any
    environment {
        PROJECT_PATH = "${env.WORKSPACE}"
        REGISTRY = "irtaza06/linuxls"
        REGISTRY_CREDENTIAL = 'dockerhub'
        TAG = 'blue'
    }
    stages {
//        stage('Clone Repository') {
//          steps {
//            git 'https://github.com/irtaza06/linuxls_project.git'
//          }
//        }
        stage('Lint Django-Project') {
            agent {
                docker {
                    image 'python:3.7.3'
                    args '--user=0:0 -v ${PROJECT_PATH}:/linuxls_project -w /linuxls_project'
                }
            }
            steps {
                sh 'pip3 install -r /linuxls_project/www/linuxls_website/requirements.txt'
                sh 'pylint /linuxls_project/www/linuxls_website/linuxls_website'
            }
        }
        stage('Lint Dockerfile') {
            agent {
                docker {
                    image 'hadolint/hadolint:latest'
                    args '-v ${PROJECT_PATH}:/linuxls_project -w /linuxls_project'
                }
            }
            steps {
                sh 'hadolint --ignore DL3009 /linuxls_project/Dockerfile'
            }
        }
        stage('Build Docker Image') {
          steps{
            script {
              dockerImage = docker.build "${REGISTRY}" + ":${TAG}"
            }
          }
        }
        
        stage('Push Docker Image') {
          steps{
            script {
              docker.withRegistry( '', "${REGISTRY_CREDENTIAL}" ) {
                dockerImage.push()
              }
            }
          }
        }
        stage('Set current kubectl context') {
            steps {
                withAWS(region:'eu-central-1', credentials:'AWS-EKS') {
                    sh './set_kubectl_context.sh'
                }
            }    
        }
        stage('Create blue RC') {
            steps {
                withAWS(region:'eu-central-1', credentials:'AWS-EKS') {
                    sh './run_blue_rc.sh'
                }
            }    
        }
        stage('Create green RC') {
            steps {
                withAWS(region:'eu-central-1', credentials:'AWS-EKS') {
                    sh './run_green_rc.sh'
                }
            }    
        }
        stage('Create bg-service/Loadbalancer') {
            steps {
                withAWS(region:'eu-central-1', credentials:'AWS-EKS') {
                    sh './run_bg_svc.sh'
                }
            }    
        }

//        stage('Create an alias record') {
//            steps {
//                withAWS(region:'eu-central-1', credentials:'AWS-EKS') {
//                    sh './create_alias_record.sh'
//                }
//            }    
//        }
        
        stage('Update service/redirect to green') {
            input {
                message "continue?"
                ok "Yes"
                submitter "irtaza06"
            }
            steps {
                withAWS(region:'eu-central-1', credentials:'AWS-EKS') {
                    sh './run_bg_svc_update.sh'
                }
            } 
        }
        stage('Remove Image Locally') {
          steps{
            sh "docker rmi ${REGISTRY}:${TAG}"
          }
        }
        
    }
}
