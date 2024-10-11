import jetbrains.buildServer.configs.kotlin.*
import jetbrains.buildServer.configs.kotlin.buildFeatures.perfmon
import jetbrains.buildServer.configs.kotlin.buildSteps.script
import jetbrains.buildServer.configs.kotlin.projectFeatures.buildReportTab
import jetbrains.buildServer.configs.kotlin.triggers.vcs
import jetbrains.buildServer.configs.kotlin.vcs.GitVcsRoot

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
    description = "Contains all other projects"

    features {
        buildReportTab {
            id = "PROJECT_EXT_1"
            title = "Code Coverage"
            startPage = "coverage.zip!index.html"
        }
    }

    cleanup {
        baseRule {
            preventDependencyCleanup = false
        }
    }

    subProject(BuildpipelinesVbazhan)
}


object BuildpipelinesVbazhan : Project({
    name = "Buildpipelines_vbazhan"

    vcsRoot(BuildpipelinesVbazhan_HttpsGithubComMarcobehlerjetbrainsBuildpipelinesRefsHeadsMain)

    buildType(BuildpipelinesVbazhan_BuildVbazh)
})

object BuildpipelinesVbazhan_BuildVbazh : BuildType({
    name = "Build_vbazh"

    params {
        password("env.AWS_SECRET_ACCESS_KEY", "credentialsJSON:efd1a0b4-9738-438f-ac49-2ef966ec0756")
        password("env.AWS_ACCESS_KEY_ID", "credentialsJSON:d64f5c40-dbf5-42a9-9595-87197292248f")
    }

    vcs {
        root(BuildpipelinesVbazhan_HttpsGithubComMarcobehlerjetbrainsBuildpipelinesRefsHeadsMain)
    }

    steps {
        script {
            name = "my_first_step"
            id = "my_first_step"
            scriptContent = """
                cd calculator-service
                mvn clean package
                aws s3 cp target/*.jar s3://aws-s3-bucket-for-snd-and-lambda-vbazh1/
            """.trimIndent()
        }
    }

    triggers {
        vcs {
        }
    }

    features {
        perfmon {
        }
    }
})

object BuildpipelinesVbazhan_HttpsGithubComMarcobehlerjetbrainsBuildpipelinesRefsHeadsMain : GitVcsRoot({
    name = "https://github.com/marcobehlerjetbrains/buildpipelines#refs/heads/main"
    url = "https://github.com/marcobehlerjetbrains/buildpipelines"
    branch = "refs/heads/main"
    branchSpec = "refs/heads/*"
})
