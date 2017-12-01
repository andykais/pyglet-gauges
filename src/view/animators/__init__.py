from . import ArcGauge, HalfCircleWideNeedle, Background
modules = [ArcGauge, HalfCircleWideNeedle, Background]

animatorClasses = {module.animator.id: module.animator for (_, module) in enumerate(modules)}
