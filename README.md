# Optimal cantilever retaining wall designs

These are my forays into the subject.

Present efforts are towards formulating models,
but I am susceptible to serendipitous injunctions of inspiration.

<!-- omit in toc -->
## Contents

- [Models](#models)
- [Reproducibility](#reproducibility)
- [Citing](#citing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Models

<!-- omit in toc -->
### Stability-constrained economic proportioning (SCEP)

SCEP proportions a wall
such that its cross-sectional area is minimized
while keeping its corresponding safety factors against failure modes
within required values.

SCEP variant 1
will be released soon.

SCEP variant 2
(see [`mod__scep-02.ipynb`](./mod__scep-02.ipynb))
considers the
toe length, heel length,
stem height, footing thickness,
and
stem thicknesses (at the base and at the tip)
as optimization variables.

## Reproducibility

For reproducibility,
use [`env.yml`]("./env.yml)
to set up a conda environment with
Python,
JupyterLab,
NumPy,
and
SciPy.

## Citing

Should you wish to cite this work
(or any of the models presented herein),
use

> Cahig, C.
> (2026, June 12).
> *Optimal cantilever retaining wall designs*.
> GitHub.
> Retrieved June 14, 2026,
> from https://github.com/christian-cahig/OptiCantiRetWall

with the applicable access date.
If you are using LaTeX,
use the following BibLaTeX entry.

```bibtex
@Online{OptiCantiRetWall,
  author       = {Christian {Cahig}},
  date         = {2026-06-12},
  title        = {Optimal cantilever retaining wall designs},
  url          = {https://github.com/christian-cahig/OptiCantiRetWall},
}
```

## License

This repository is licensed under the
[Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/).
See [`LICENSE`](./LICENSE) for the details.

## Contact

You may open an issue to
raise questions, share thoughts, and start discussions.
You can also get in touch through
[christian.cahig@outlook.com](mailto:christian.cahig@outlook.com).

## Acknowledgements

This side quest
sprang from being nerd-sniped by
Norence Zyron Bedasua,
Asia Sky Grigsby,
and
Adrian Rey Magsanay
in the course of doing their undergraduate research
at
[Mindanao State University - Iligan Institute of Technology](https://www.msuiit.edu.ph/).

Their advisors —
Kenny Cantila,
Ervin Cristobal,
and
Minette Merca —
have also been supportive
that they deserve a spotlight of appreciation.

Serg Jason Bodiongan
and
Joel Opon
have been generous with sundry ideas
on cantilever retaining walls and geotechnics in general.
