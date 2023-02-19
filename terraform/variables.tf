variable "aws" {
  description = "AWS Environment details"
  type = object({
    environment = string
    profile = string
    region = string
  })
}
