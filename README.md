<h1 align="center">
  <img src="https://dashboard.snapcraft.io/site_media/appmedia/android-studio-canary.png" alt="Android Studio Canary">
  <br />
  Android Studio Canary
  <br />
</h1>

<p align="center"><b>This is the snap for Android Studio Canary</b>, <em>"The IDE for Android (Canary build)"</em>. It works on Ubuntu, Fedora, Debian, and other major Linux distributions.</p>

<p align="center">
<a href="https://snapcraft.io/android-studio-canary">
  <img alt="enrol me" src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg" />
</a>
</p>

## Install

    sudo snap install android-studio-canary --classic

([Don't have snapd installed?](https://snapcraft.io/docs/core/install))

## How to contribute

### Reporting issues

Please [open an issue](https://github.com/snapcrafters/android-studio-canary/issues/new/choose) if you find a bug, have a feature request, or if the snap is out of date.

### Updating the snap

Snap versions are [automatically kept in sync](https://github.com/snapcrafters/android-studio-canary/actions/workflows/sync-version-with-upstream.yml) with upstream releases. If you want to manually update the snap, you can [open a pull request](https://github.com/snapcrafters/android-studio-canary/compare) against the `candidate` branch.

When your pull request is merged, the snap will be automatically built and published to the [candidate channel](https://snapcraft.io/android-studio-canary) in the Snap Store. After a period of testing, a maintainer will promote the snap to the stable channel.

### Testing

If you want to help test new releases of the snap, you can subscribe to the [candidate channel](https://snapcraft.io/android-studio-canary) and [leave a comment](https://github.com/snapcrafters/android-studio-canary/issues) with your testing results.

    sudo snap install android-studio-canary --channel=candidate --classic

## License

The scripts and documentation in this project are released under the [MIT License](LICENSE).
