resource "aws_vpc" "vpc" {
  cidr_block           = "10.75.0.0/16"
  enable_dns_hostnames = true
}
