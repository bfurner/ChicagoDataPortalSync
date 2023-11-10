from typing import List, Optional
from pydantic import BaseModel, Json, validator
from datetime import datetime


class UserPerson(BaseModel):
    id: Optional[str] = None
    displayName: Optional[str] = None

class SubmissionDetail(BaseModel):
    permissionType: str

class SubmissionOutcomeApplication(BaseModel):
    endedAt: Optional[int] = None
    failureCount: Optional[int] = None
    startedAt: Optional[int] = None
    status: str

class Approval(BaseModel):
    reviewedAt: Optional[int] = None
    reviewedAutomatically: bool
    state: str
    submissionId: int
    submissionObject: str
    submissionOutcome: str
    submittedAt: int
    targetAudience: str
    workflowId: int
    reviewer: Optional[UserPerson] = None
    submissionDetails: SubmissionDetail
    submissionOutcomeApplication: SubmissionOutcomeApplication
    submitter: Optional[UserPerson] = None

class DataSet(BaseModel):
    id: str
    name: str
    attribution: Optional[str] = None
    attributionLink: Optional[str] = None 
    category: Optional[str] = None
    createdAt: datetime
    dataUpdatedAt: Optional[datetime] = None
    dataUri: str
    description: Optional[str] = None
    domain: str
    externalId: Optional[str] = None
    hideFromCatalog: bool = False
    hideFromDataJson: bool = False
    license: Optional[str] = None
    metadataUpdatedAt: datetime = None
    provenance: Optional[str] = None
    updatedAt: datetime = None
    webUri: str = None
    approvals: List[Approval] = None
    customFields: Optional[dict] = None
    tags: Optional[List[str]] = None

class DataSetList(BaseModel):
    datasets: Json[List[DataSet]]



