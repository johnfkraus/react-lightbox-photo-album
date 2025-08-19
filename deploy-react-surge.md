# Deploying a React app with Surge (from Create React App format)

**1. Make sure you have surge installed globally**

- `npm install -g surge`

**2. Run the Create React App build**

- `cd your-react-project`
- `npm run build`

**3. Change into build directory**

- `cd build`

**4. Run surge**
 
 - `surge`
 - Log in with your email and password, hit enter
 - Enter the correct path to your project, hit enter
 - Change the url to your custom url or use the default, hit enter
 - Surge will run deploy

### Adding deploy script to package.json

- In package.json under "scripts" add this line:
- `"deploy": "npm run build && surge ./build/ your-surge-url.surge.sh"`
- Update `your-surge-url` with your url
- `npm run deploy` (this will need to be run from your project root, not the build directory!)
