# alpine 3.22.2
FROM alpine:latest 

RUN apk update && apk upgrade

# Install dust
RUN apk add rust cargo

# Install bun
RUN apk add unzip curl bash
RUN curl -fsSL https://bun.sh/install | bash && apk del --purge -r unzip bash
ENV PATH="$PATH:/root/.bun/bin/"

# Install python 
RUN apk add python3 uv

# Install tauri dependencies
RUN apk add build-base webkit2gtk-4.1-dev curl wget file openssl libayatana-appindicator-dev librsvg font-freefont 

# # Set up Android SDK

# ## Prepare Android directories and system variables
# ENV ANDROID_HOME="/Android/sdk"
# ENV NDK_VERSION="28.2.13676358"
# ENV NDK_HOME="$ANDROID_HOME/ndk/$NDK_VERSION"
# ENV PATH="$PATH:$ANDROID_HOME/platform-tools"
# ENV PATH="$PATH:$ANDROID_HOME/cmdline-tools/latest/bin"
# RUN mkdir -p .android && touch .android/repositories.cfg

# ## Install rust android target
# RUN rustup target add aarch64-linux-android armv7-linux-androideabi i686-linux-android x86_64-linux-android

# ## Install jdk, android ndk and android tools
# RUN apt-get install -y default-jdk
# RUN curl -fsSL -o sdk-tools.zip https://dl.google.com/android/repository/commandlinetools-linux-13114758_latest.zip
# RUN unzip sdk-tools.zip && rm sdk-tools.zip
# RUN mkdir -p $ANDROID_HOME/cmdline-tools && mv cmdline-tools $ANDROID_HOME/cmdline-tools/latest

# RUN yes | sdkmanager --licenses && sdkmanager "ndk;$NDK_VERSION" "platform-tools"