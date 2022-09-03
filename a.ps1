Copy-Item $args[0] -Destination $args[0]+".ps1"
& $args[0]+".ps1"