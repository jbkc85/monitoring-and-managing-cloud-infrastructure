variable "aws" {
  description = "AWS Environment details"
  type = object({
    environment = string
    profile = string
    region = string
  })
}

variable "public_zone" {
  description = "AWS Route53 Public Zone ID"
  type = string
}
