# react-lightbox-photo-album

The live website is here: https://johns-photo-album.surge.sh/

The starting point for this website project was the lightbox example in this repository: https://github.com/igordanchenko/react-photo-album

Your photos for the photo album need to be uploaded to S3 or similar location.  Configure the S3 bucket URL in the src/photos.tsx file.

Deployed to Surge.sh

To get the SURGE_TOKEN, run:

surge token

Configure SURGE_TOKEN as a Github secret.

Commiting changes to main updates the live website using Github actions.

Run in development mode:

npm run dev

To deploy on Surge.sh:

Prerequisites:

- A Surge.sh account and domain (see Surge.sh for details).
- A Github.com repository for this project.

In your Github repository, under Settings > Secrets and variables > Repository secrets, configure the following Repository secrets:

SURGE_DOMAIN <br>
SURGE_TOKEN

Commit the code to the main branch in your Github repository to trigger the .github/workflows/deploy.yml script.
```shell
git add .
git commit -m 'your commit message'
git push
```
