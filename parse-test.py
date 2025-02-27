from lexer import lexer 
from parser import parser
j = 0

def test_parser(input_data, expected_output):
    
    result = parser.parse(input_data, lexer=lexer)

    # for classItem in result:
    #     for key, value in classItem.items():
    #         print(f"{Fore.GREEN}Class: {key}")
            
    #         for internalKey in value:
    #             print(f"{Fore.BLUE}    {internalKey}")


# Teste Unitarios para classes primitivas
# Exemplo 1: Declaração de uma classe primitiva

input_data_1 = """
Class: Activity
   
    SubClassOf: 
        FunctionalComplex,
        participatedIn some xsd:integer
    
    
Class: Actor
  
    SubClassOf: 
        FunctionalComplex,
        participatedIn some xsd:integer,
        participatedOn some xsd:string,
        participatedIn some DataExchange
    
    
Class: BrokerServiceProvider

        
    SubClassOf: 
        IntermediaryParticipant,
        mediates some MetadataAssignment,
        mediates some MetadataRetrival
    
    
Class: Certificate
    
    SubClassOf: 
        Resource,
        mediates some CertificationAct
    
    
Class: Certification
    SubClassOf: 
        Activity,
        historicallyDependsOn only CertificationAct,
        historicallyDependsOn exactly 1 CertificationAct
    
    
Class: CertificationAct

        
    EquivalentTo: 
        Relator
         and (historicallyDependsOn only EvaluationReport)
         and (mediates only (Certificate or CertificationBody or Evaluated))
         and (mediates min 1 Certificate)
         and (mediates min 1 CertificationBody)
         and (mediates min 1 Evaluated)
         and (historicallyDependsOn min 1 Certification)
         and (historicallyDependsOn exactly 1 EvaluationReport)
    
    
Class: CertificationBody

        
    SubClassOf: 
        IntermediaryParticipant,
        emitsCertificate some Certificate,
        mediates some CertificationAct
    
    
Class: ConditionalClaim

        
    SubClassOf: 
        IntrinsicMode,
        (inheresIn only DataCustomer) and (externallyDependsOn only DataSupplier) and (historicallyDependsOn only MetadataRetrival),
        historicallyDependsOn min 1 MetadataRetrival,
        inheresIn exactly 1 DataCustomer,
        externallyDependsOn exactly 1 DataSupplier
    
    
Class: ConditionalCommitment
    
    SubClassOf: 
        IntrinsicMode,
        (inheresIn only DataSupplier) and (externallyDependsOn only DataCustomer) and (historicallyDependsOn only MetadataAssignment),
       	historicallyDependsOn some MetadataAssignment,
        inheresIn exactly 1 DataSupplier,
        externallyDependsOn exactly 1 DataCustomer
    
    
Class: Connector

        
    SubClassOf: 
        Resource,
        mediates some InvokeDataOperation,
        enforces min 1 DataUsagePolicy
    
    
Class: CoreParticipant

        
    SubClassOf: 
        Actor
    
    
Class: Counterpart

        
    SubClassOf: 
        Resource,
        historicallyDependsOn some OffereeUnconditionalAgreement
    
    
Class: CounterpartContribution

        
    SubClassOf: 
        Event,
        participatedIn only DataCustomer,
        participatedIn min 1 DataCustomer
    
    
Class: CounterpartContributionType

        
    SubClassOf: 
        ConcreteIndividualType,
        instantiate some CounterpartContribution,
        instantiate only CounterpartContribution
    
    
Class: Data

        
    SubClassOf: 
        Resource,
        inheresIn some Metadata,
        inverse mediates some DataSovereigntyAct,
        inverse mediates some InvokeDataOperation,
        inverse mediates exactly 1 Ownership
    
    
Class: DataCustomer

        
    SubClassOf: 
        CoreParticipant,
        externallyDependsOn some ConditionalCommitment,
        externallyDependsOn some OfferorUnconditionalAgreement,
        participatedIn some Offer,
        calls some DataOperation,
        inheresIn some ConditionalClaim,
        inheresIn some OffereeUnconditionalAgreement,
        mediates some EconomicOffering,
        mediates some InvokeDataOperation,
        mediates some MetadataRetrival
    
    DisjointWith: 
        DataSupplier
    
    
Class: DataExchange

        
    EquivalentTo: 
        Event
         and (participatedIn some Activity)
         and (participatedIn some Resource)
         and (participatedIn min 1 DataCustomer)
         and (participatedIn min 1 DataSupplier)
         and (participatedIn min 2 Actor)
         and (composedBy exactly 1 CounterpartContribution)
         and (composedBy exactly 1 OfferedContribution)
    
    
Class: DataOperation

       
    SubClassOf: 
        Activity,
         mediates some InvokeDataOperation,
         mediates only InvokeDataOperation
    
    
Class: DataSovereigntyAct

        
    SubClassOf: 
        Relator,
        mediates some Data,
        mediates some DataUsagePolicy,
        mediates min 1 DataSupplier
    
    
Class: DataSupplier

        
    SubClassOf: 
        CoreParticipant,
        externallyDependsOn some ConditionalClaim,
        externallyDependsOn some OffereeUnconditionalAgreement,
        participatedIn some Offer,
        creates some DataUsagePolicy,
        owns some Data,
        responds some DataOperation,
        inheresIn some ConditionalCommitment,
        inheresIn some OfferorUnconditionalAgreement,
        mediates some DataSovereigntyAct,
        mediates some EconomicOffering,
        mediates some MetadataAssignment,
        mediates some Ownership
    
    DisjointWith: 
        DataCustomer
    
    
Class: DataUsagePolicy

        
    SubClassOf: 
        Resource,
        mediates some DataSovereigntyAct,
        mediates some InvokeDataOperation
    
    
Class: DigitalAsset

        
    SubClassOf: 
        Resource,
        (composedBy exactly 1 Data) and (composedBy exactly 1 DataUsagePolicy),
        historicallyDependsOn some OfferorUnconditionalAgreement
    
    
Class: EconomicAgreement

        
    EquivalentTo: 
        Relator
         and ((composedBy some OffereeUnconditionalAgreement)
                and (composedBy some OfferorUnconditionalAgreement))
         and (historicallyDependsOn only EconomicOffering)
         and (composedBy only (OffereeUnconditionalAgreement or OfferorUnconditionalAgreement))
         and (historicallyDependsOn min 1 EconomicOffering)
    
    
Class: EconomicOffering

        
    EquivalentTo: 
        Relator
         and ((composedBy some ConditionalClaim) and (composedBy some ConditionalCommitment))
         
Class: Evaluated

    EquivalentTo: 
        BrokerServiceProvider or Connector or CoreParticipant
    
    SubClassOf: 
        FunctionalComplex
    
    
Class: Evaluation

        
    SubClassOf: 
        Activity,
        historicallyDependsOn only EvaluationAct,
        historicallyDependsOn exactly 1 EvaluationAct
    
    
Class: EvaluationAct

        
    EquivalentTo: 
        Relator
         and (mediates only (Evaluated or EvaluationFacility or EvaluationReport))
         and (mediates min 1 Evaluated)
         and (mediates min 1 EvaluationFacility)
         and (mediates min 1 EvaluationReport)
         and (historicallyDependsOn min 1 Evaluation)
    
    
Class: EvaluationFacility

        
    SubClassOf: 
        IntermediaryParticipant,
        emitsReport some EvaluationReport,
        mediates some EvaluationAct
    
    
Class: EvaluationReport

        
    SubClassOf: 
        Resource,
        mediates some EvaluationAct
    
    
Class: IntermediaryParticipant

        
    SubClassOf: 
        Actor
    
    
Class: InvokeDataOperation

        
    SubClassOf: 
        Relator,
        mediates some Data,
        mediates min 1 Connector,
        mediates min 1 DataCustomer,
        mediates min 1 DataOperation,
        mediates min 1 DataSupplier,
        mediates min 1 DataUsagePolicy
    
    
Class: Metadata

        
    SubClassOf: 
        Resource,
        describes some Data,
        mediates exactly 1 MetadataAssignment,
        mediates exactly 1 MetadataRetrival
    
    
Class: MetadataAssignment

        
    SubClassOf: 
        Relator,
        inheresIn min 1 ConditionalCommitment,
        mediates min 1 BrokerServiceProvider,
        mediates min 1 DataSupplier,
        mediates min 1 Metadata
    
    
Class: MetadataRetrival

        
    SubClassOf: 
        Relator,
        inheresIn some ConditionalClaim,
        mediates min 1 BrokerServiceProvider,
        mediates min 1 DataCustomer,
        mediates min 1 Metadata
    
    
Class: Offer

        
    EquivalentTo: 
        Event
         and participatedIn only (DataCustomer or DataSupplier)
         and wasCreatedIn only EconomicOffering
         and participatedIn min 1 DataCustomer
         and participatedIn min 1 DataSupplier
         and wasCreatedIn exactly 1 EconomicOffering
    
    
Class: OfferedContribution

        
    SubClassOf: 
        Event,
        participatedIn only DataSupplier,
        participatedIn min 1 DataSupplier
    
    
Class: OfferedContributionType

        
    SubClassOf: 
        ConcreteIndividualType,
        instantiate some OfferedContribution,
        instantiate only OfferedContribution
    
    
Class: OffereeUnconditionalAgreement

        
    SubClassOf: 
        IntrinsicMode,
        (externallyDependsOn only CounterpartContributionType) and (historicallyDependsOn only Counterpart) and (inheresIn only DataCustomer),
        externallyDependsOn some CounterpartContributionType,
        historicallyDependsOn min 1 Counterpart,
        inheresIn exactly 1 DataCustomer
    
    
Class: OfferorUnconditionalAgreement

        
    SubClassOf: 
        IntrinsicMode,
        (externallyDependsOn only OfferedContributionType) and (historicallyDependsOn only DigitalAsset) and (inheresIn only DataSupplier),
        externallyDependsOn some OfferedContributionType,
        historicallyDependsOn min 1 DigitalAsset,
        inheresIn exactly 1 DataSupplier
    
    
Class: Ownership

        
    SubClassOf: 
        Relator,
        mediates some Data,
        mediates min 1 DataSupplier
    
    
Class: Resource

        
    SubClassOf: 
        FunctionalComplex,
        participatedIn some DataExchange
"""

test_parser(input_data_1, "")

# print(classes_tree)
