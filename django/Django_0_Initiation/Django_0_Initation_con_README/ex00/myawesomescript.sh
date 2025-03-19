
# Choice of interpreter
#!/bin/sh

# Check if an argument (URL) has been provided
if [ -z "$1" ]; then
  echo "Usage: $0 <bit.ly URL>" >&2
  exit 1
fi

# Get the final URL after redirects
curl -Ls -o /dev/null -w %{url_effective} "$1"


# ./myawesomescript.sh bit.ly/1O72s3U
