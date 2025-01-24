provider "aws" {
  region = "us-west-2"
}

resource "aws_sagemaker_domain" "ai_dev" {
  domain_name = "ai-assisted-dev"
  auth_mode   = "IAM"
  vpc_id      = aws_vpc.main.id
  
  default_user_settings {
    execution_role = aws_iam_role.sagemaker_role.arn
  }
}