resource "aws_vpc" "main" {
  cidr_block = var.cidr_block

  tags = {
    Name = "Main_VPC"
  }
}

resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id
  cidr_block = cidrsubnet(var.cidr_block, 8, 1)

  tags = {
    Name = "Main_Subnet"
  }
}

output "subnet_id" {
  value = aws_subnet.main.id
}

output "subnet_ids" {
  value = [aws_subnet.main.id]
}
