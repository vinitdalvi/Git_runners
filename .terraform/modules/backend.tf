terraform {
  backend "s3" {
    bucket = "nani-parthu-nan"
    key    = "path/to/my/key"
    region = "us-east-1"
  }
}
