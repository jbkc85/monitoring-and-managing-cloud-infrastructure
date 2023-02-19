#
# provider.aws
# provider initialized for all AWS interactions
provider "aws" {
  profile = var.aws.profile
  region  = var.aws.region

  default_tags {
    tags = {
      Environment = var.aws.environment
      Region = var.aws.region
      ManagedBy = "terraform"
    }
  }
}

data "aws_caller_identity" "current" {}
