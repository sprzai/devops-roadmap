variable "cidr_block" {
  description = "CIDR block for the VPC"
}

variable "ami" {
  description = "The ID of the AMI to use"
}

variable "instance_type" {
  description = "The type of instance to start"
}

variable "key_name" {
  description = "The key pair to use"
}
