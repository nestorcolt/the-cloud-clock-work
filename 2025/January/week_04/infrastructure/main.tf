terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_sagemaker_domain" "ai_dev" {
  domain_name = var.domain_name
  auth_mode   = "IAM"
  vpc_id      = aws_vpc.main.id
  
  default_user_settings {
    execution_role = aws_iam_role.sagemaker_role.arn
  }
}