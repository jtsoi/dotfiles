
export GITHUB_USER="{{ github.user }}"
export GITHUB_PACKAGES_TOKEN="{{ github.packages_token }}"

alias docker-login-github='docker login -u $GITHUB_USER -p $GITHUB_PACKAGES_TOKEN docker.pkg.github.com'
alias bundle-login-github='bundle config rubygems.pkg.github.com $GITHUB_USER:$GITHUB_PACKAGES_TOKEN'
