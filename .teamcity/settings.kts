version = "2023.05"

//project {
//    buildType(BuildAndTest)
//    buildType(DockerBuild)
//    buildType(RunDockerContainer)
//
//    vcsRoot(GitHubVcs)
//
//    // Build configuration for "Build & Test"
//    object BuildAndTest : BuildType({
//        name = "Build & Test"
//
//        vcs {
//            root(GitHubVcs)
//        }
//
//        steps {
//            script {
//                name = "Download JAR from S3"
//                scriptContent = """
//                    ./build_s3_download.sh
//                """
//            }
//            script {
//                name = "Run tests"
//                scriptContent = """
//                    ./run_tests.sh
//                """
//            }
//        }
//
//        triggers {
//            vcs {
//                branchFilter = "+:teamcity_cicd"
//            }
//        }
//    })
//
//    // Build configuration for "Docker Build"
//    object DockerBuild : BuildType({
//        name = "Docker Build"
//
//        vcs {
//            root(GitHubVcs)
//        }
//
//        steps {
//            script {
//                name = "Build Docker Image"
//                scriptContent = """
//                    docker build -t your-spark-app .
//                """
//            }
//        }
//
//        triggers {
//            finishBuildTrigger {
//                buildType = "BuildAndTest"
//            }
//        }
//    })
//
//    // Build configuration for "Run Docker Container"
//    object RunDockerContainer : BuildType({
//        name = "Run Docker Container"
//
//        vcs {
//            root(GitHubVcs)
//        }
//
//        steps {
//            script {
//                name = "Run Scala in Docker"
//                scriptContent = """
//                    ./scala_run.sh
//                """
//            }
//        }
//
//        triggers {
//            finishBuildTrigger {
//                buildType = "DockerBuild"
//            }
//        }
//    })
//
//    // VCS Root configuration for GitHub
//    object GitHubVcs : GitVcsRoot({
//        name = "GitHub Repo"
//        url = "https://github.com/your_username/trainee_devops_tasks.git"
//        branch = "refs/heads/teamcity_cicd"
//    })
//}
