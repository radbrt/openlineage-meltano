# Meltano OpenLineage
Meltano-OpenLineage is a meltano utility extension for Open Lineage

## ⚠️ WARNING ⚠️
This project is highly experimental and nowhere near ready for anything at all. Also, this isn't really a project I'm interested in maintaining long-term. Other people are probably more right for that. So absolutely not, under any circumstance whatsoever make this project a dependence for anything at all. Feel free to fork or copy-paste the code you like instead.

## How this works so far
Prerequisites: You need a meltano project, that contains a logging file that specifies file logging output with json format. The plugin will find the log-file from this. The log-level must be pretty low, at least `INFO` level logging must be enabled.

Steps to run:
1. Install the extension, so that you get the `openlineage_parser` cli command in your path.
2. Go to your meltano project, and run `meltano compile` if you haven't already done so. This generates the manifest files we use.
3. If you want to log to a password-protected marquez server, create an env variable `MARQUEZ_API_KEY` with your bearer token.
4. Run `openlineage_parser` with the following options:
  - `--environment`: name of the meltano environment you want to parse (this will refer to the manifest files)
  - `--url`: Full URL+endpoint to the marquez server you want to write lineage to. Default `http://localhost:5000/api/v1/lineage`
  - `--publish`: Bool flag wether or not to post lineage data to the marquez endpoint.

## Help in development
I am adding a bunch of issues (and possible some discussion). I won't go into details about that here, but there are some general topics:
- Currently, this extension doesn't even work. The basic CLI commands can be invoked, but the `meltano invoke` thing doesn't. This is probably a trivial technical thing I haven't understood yet.
- There are some fixes that can be done to the utility itself, for instance filling in better values for things like schema URL etc. Openlineage seems to assume there are websites everywhere, or that you buy into a semanticWeb type of thing where everything is a URL but nothing is a website.
- There are some improvements that require help from either the Meltano library itself, the Meltano SDK, or stuff like naming convensions in taps/targets.

*Please, please add thoughts and ideas in the issues or discussion section.*

## Installing this extension for local development

1. Install the project dependencies with `poetry install`:

```shell
cd path/to/your/project
poetry install
```

2. Verify that you can invoke the extension:

```shell
poetry run openlineage_extension --help
poetry run openlineage_extension describe --format=yaml
poetry run openlineage_invoker --help # if you have are wrapping another tool
```

## Template updates

This project was generated with [copier](https://copier.readthedocs.io/en/stable/) from the [Meltano EDK template](https://github.com/meltano/edk).
Answers to the questions asked during the generation process are stored in the `.copier_answers.yml` file.

Removing this file can potentially cause unwanted changes to the project if the supplied answers differ from the original when using `copier update`.
