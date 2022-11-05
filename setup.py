from setuptools import setup # type: ignore

setup(
    name='FiniteAutomaton',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'FAInteractive=FAInteractive:run',
            'RCInteractive=RCInteractive:run'
        ]
    }
)