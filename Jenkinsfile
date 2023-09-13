node {
        stage('SCM') {
                checkout scm
        }
	
        stage('SQ-99') {
                def scannerHome = tool 'CLI';
                withSonarQubeEnv('SQ-99') {
			bat "${scannerHome}\\bin\\sonar-scanner.bat -Dsonar.verbose=true"
                }
        }
}
