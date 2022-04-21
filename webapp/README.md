# Working with the Web App

## development environment

From this folder, run:

```bash
$ npm init
```

To run the webpack development server:

```bash
$ npm run start
```

Note that you should run the Flask application separately
and append `?test=1` to the dev url that launches in the browser.

## Releasing

To build a new bundle, run:

```bash
$ npm run build
```

This will build the new bundle and deploy it to
`walldisplay_calendar/static/*`.  This should be committed.
