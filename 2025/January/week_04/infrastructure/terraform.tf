terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_sagemaker_domain" "ai_dev" {
  domain_name = "ai-assisted-dev"
  auth_mode   = "IAM"
  vpc_id      = aws_vpc.main.id
}