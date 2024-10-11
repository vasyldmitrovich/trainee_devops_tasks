import jetbrains.buildServer.configs.kotlin.*
import jetbrains.buildServer.configs.kotlin.buildFeatures.perfmon
import jetbrains.buildServer.configs.kotlin.buildSteps.dockerCommand
import jetbrains.buildServer.configs.kotlin.buildSteps.script
import jetbrains.buildServer.configs.kotlin.buildSteps.maven
import jetbrains.buildServer.configs.kotlin.triggers.vcs

/*
The settings script is an entry point for defining a TeamCity
project hierarchy. The script should contain a single call to the
project() function with a Project instance or an init function as
an argument.

VcsRoots, BuildTypes, Templates, and subprojects can be
registered inside the project using the vcsRoot(), buildType(),
template(), and subProject() methods respectively.

To debug settings scripts in command-line, run the

    mvnDebug org.jetbrains.teamcity:teamcity-configs-maven-plugin:generate

command and attach your debugger to the port 8000.

To debug in IntelliJ Idea, open the 'Maven Projects' tool window (View
-> Tool Windows -> Maven Projects), find the generate task node
(Plugins -> teamcity-configs -> teamcity-configs:generate), the
'Debug' option is available in the context menu for the task.
*/

version = "2024.03"

project {

    buildType(Build)
}

object Build : BuildType({
    name = "Build"

    params {
        password("env.AWS_SECRET_ACCESS_KEY", "credentialsJSON:efd1a0b4-9738-438f-ac49-2ef966ec0756")
        password("env.AWS_ACCESS_KEY_ID", "credentialsJSON:d64f5c40-dbf5-42a9-9595-87197292248f")
    }

    vcs {
        root(DslContext.settingsRoot)
        cleanCheckout = true // Add Clean Checkout for all build
    }

    steps {
        script {
            name = "Get JAR from S3"
            id = "simpleRunner"
            scriptContent = """
                chmod +x ./src.teamcity_builds/build_s3_download.sh
                ./src.teamcity_builds/build_s3_download.sh
            """.trimIndent()
        }
        maven {
            name = "Maven Build"
            goals = "clean package"
            workingDir = "./userstoryproj_back"  // Path to maven project
            jdkHome = "%env.JAVA_HOME%"
        }
        script {
            name = "Run tests"
            id = "simpleRunner_1"
            scriptContent = """
                chmod +x ./src.teamcity_builds/run_tests.sh
                ./src.teamcity_builds/run_tests.sh
            """.trimIndent()
        }
        dockerCommand {
            name = "Build docker container"
            id = "DockerCommand"
            enabled = false
            commandType = build {
                source = file {
                    path = "src.teamcity_builds/Dockerfile"
                }
            }
        }
        script {
            id = "simpleRunner_2"
            scriptContent = "./src.teamcity_builds/scala_run.sh"
        }
    }

    triggers {
        vcs {
            triggerRules = "+:."
            branchFilter = "+:teamcity_cicd"
            perCheckinTriggering = true
            groupCheckinsByCommitter = true
            enableQueueOptimization = false
        }
    }

    features {
        perfmon {
        }
    }
})
