
import FWCore.ParameterSet.Config as cms

#for now Shashlik uses EE timing
from particleFlowClusterECALTimeResolutionParameters_cfi import  _timeResolutionShashlikEndcap
#until we are actually clustering across the EB/EE boundary
#it is faster to cluster EB and EE as separate

particleFlowRecHitEK = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string("PFRecHitShashlikNavigatorWithTime"),
        noiseLevel = cms.double(0.027),   
        noiseTerm  = cms.double(36.1),
        constantTerm = cms.double(10),
        sigmaCut = cms.double(5.0),
        timeResolutionCalc = _timeResolutionShashlikEndcap,
        barrel = cms.PSet( ),
        endcap = cms.PSet( )
    ),
    producers = cms.VPSet(
           cms.PSet(
             name = cms.string("PFEKRecHitCreator"),
             src  = cms.InputTag("ecalRecHit:EcalRecHitsEK"),
             qualityTests = cms.VPSet( 
                cms.PSet(
                  name = cms.string("PFRecHitQTestThreshold"),
                  threshold = cms.double(0.08)
                  ),
                cms.PSet(
                  name = cms.string("PFRecHitQTestShashlikTiming"),
                  UseSafetyCuts = cms.bool(True),
                  BadTimingEThreshold = cms.double(0.250)
                  )
                )             
           )          
    )          
)
