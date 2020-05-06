# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class KeyVaultSecretStatus(str, Enum):

    initialized = "Initialized"
    waiting_on_certificate_order = "WaitingOnCertificateOrder"
    succeeded = "Succeeded"
    certificate_order_failed = "CertificateOrderFailed"
    operation_not_permitted_on_key_vault = "OperationNotPermittedOnKeyVault"
    azure_service_unauthorized_to_access_key_vault = "AzureServiceUnauthorizedToAccessKeyVault"
    key_vault_does_not_exist = "KeyVaultDoesNotExist"
    key_vault_secret_does_not_exist = "KeyVaultSecretDoesNotExist"
    unknown_error = "UnknownError"
    external_private_key = "ExternalPrivateKey"
    unknown = "Unknown"


class CertificateProductType(str, Enum):

    standard_domain_validated_ssl = "StandardDomainValidatedSsl"
    standard_domain_validated_wild_card_ssl = "StandardDomainValidatedWildCardSsl"


class ProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    in_progress = "InProgress"
    deleting = "Deleting"


class CertificateOrderStatus(str, Enum):

    pendingissuance = "Pendingissuance"
    issued = "Issued"
    revoked = "Revoked"
    canceled = "Canceled"
    denied = "Denied"
    pendingrevocation = "Pendingrevocation"
    pending_rekey = "PendingRekey"
    unused = "Unused"
    expired = "Expired"
    not_submitted = "NotSubmitted"


class CertificateOrderActionType(str, Enum):

    certificate_issued = "CertificateIssued"
    certificate_order_canceled = "CertificateOrderCanceled"
    certificate_order_created = "CertificateOrderCreated"
    certificate_revoked = "CertificateRevoked"
    domain_validation_complete = "DomainValidationComplete"
    fraud_detected = "FraudDetected"
    org_name_change = "OrgNameChange"
    org_validation_complete = "OrgValidationComplete"
    san_drop = "SanDrop"
    fraud_cleared = "FraudCleared"
    certificate_expired = "CertificateExpired"
    certificate_expiration_warning = "CertificateExpirationWarning"
    fraud_documentation_required = "FraudDocumentationRequired"
    unknown = "Unknown"


class RouteType(str, Enum):

    default = "DEFAULT"
    inherited = "INHERITED"
    static = "STATIC"


class ManagedServiceIdentityType(str, Enum):

    none = "None"
    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"


class IpFilterTag(str, Enum):

    default = "Default"
    xff_proxy = "XffProxy"


class AutoHealActionType(str, Enum):

    recycle = "Recycle"
    log_event = "LogEvent"
    custom_action = "CustomAction"


class ConnectionStringType(str, Enum):

    my_sql = "MySql"
    sql_server = "SQLServer"
    sql_azure = "SQLAzure"
    custom = "Custom"
    notification_hub = "NotificationHub"
    service_bus = "ServiceBus"
    event_hub = "EventHub"
    api_hub = "ApiHub"
    doc_db = "DocDb"
    redis_cache = "RedisCache"
    postgre_sql = "PostgreSQL"


class AzureStorageType(str, Enum):

    azure_files = "AzureFiles"
    azure_blob = "AzureBlob"


class AzureStorageState(str, Enum):

    ok = "Ok"
    invalid_credentials = "InvalidCredentials"
    invalid_share = "InvalidShare"


class ScmType(str, Enum):

    none = "None"
    dropbox = "Dropbox"
    tfs = "Tfs"
    local_git = "LocalGit"
    git_hub = "GitHub"
    code_plex_git = "CodePlexGit"
    code_plex_hg = "CodePlexHg"
    bitbucket_git = "BitbucketGit"
    bitbucket_hg = "BitbucketHg"
    external_git = "ExternalGit"
    external_hg = "ExternalHg"
    one_drive = "OneDrive"
    vso = "VSO"
    vstsrm = "VSTSRM"


class ManagedPipelineMode(str, Enum):

    integrated = "Integrated"
    classic = "Classic"


class SiteLoadBalancing(str, Enum):

    weighted_round_robin = "WeightedRoundRobin"
    least_requests = "LeastRequests"
    least_response_time = "LeastResponseTime"
    weighted_total_traffic = "WeightedTotalTraffic"
    request_hash = "RequestHash"


class SupportedTlsVersions(str, Enum):

    one_full_stop_zero = "1.0"
    one_full_stop_one = "1.1"
    one_full_stop_two = "1.2"


class FtpsState(str, Enum):

    all_allowed = "AllAllowed"
    ftps_only = "FtpsOnly"
    disabled = "Disabled"


class SslState(str, Enum):

    disabled = "Disabled"
    sni_enabled = "SniEnabled"
    ip_based_enabled = "IpBasedEnabled"


class HostType(str, Enum):

    standard = "Standard"
    repository = "Repository"


class UsageState(str, Enum):

    normal = "Normal"
    exceeded = "Exceeded"


class SiteAvailabilityState(str, Enum):

    normal = "Normal"
    limited = "Limited"
    disaster_recovery_mode = "DisasterRecoveryMode"


class ClientCertMode(str, Enum):

    required = "Required"
    optional = "Optional"


class RedundancyMode(str, Enum):

    none = "None"
    manual = "Manual"
    failover = "Failover"
    active_active = "ActiveActive"
    geo_redundant = "GeoRedundant"


class StatusOptions(str, Enum):

    ready = "Ready"
    pending = "Pending"
    creating = "Creating"


class DomainStatus(str, Enum):

    active = "Active"
    awaiting = "Awaiting"
    cancelled = "Cancelled"
    confiscated = "Confiscated"
    disabled = "Disabled"
    excluded = "Excluded"
    expired = "Expired"
    failed = "Failed"
    held = "Held"
    locked = "Locked"
    parked = "Parked"
    pending = "Pending"
    reserved = "Reserved"
    reverted = "Reverted"
    suspended = "Suspended"
    transferred = "Transferred"
    unknown = "Unknown"
    unlocked = "Unlocked"
    unparked = "Unparked"
    updated = "Updated"
    json_converter_failed = "JsonConverterFailed"


class AzureResourceType(str, Enum):

    website = "Website"
    traffic_manager = "TrafficManager"


class CustomHostNameDnsRecordType(str, Enum):

    cname = "CName"
    a = "A"


class HostNameType(str, Enum):

    verified = "Verified"
    managed = "Managed"


class DnsType(str, Enum):

    azure_dns = "AzureDns"
    default_domain_registrar_dns = "DefaultDomainRegistrarDns"


class DomainType(str, Enum):

    regular = "Regular"
    soft_deleted = "SoftDeleted"


class HostingEnvironmentStatus(str, Enum):

    preparing = "Preparing"
    ready = "Ready"
    scaling = "Scaling"
    deleting = "Deleting"


class InternalLoadBalancingMode(str, Enum):

    none = "None"
    web = "Web"
    publishing = "Publishing"


class ComputeModeOptions(str, Enum):

    shared = "Shared"
    dedicated = "Dedicated"
    dynamic = "Dynamic"


class WorkerSizeOptions(str, Enum):

    small = "Small"
    medium = "Medium"
    large = "Large"
    d1 = "D1"
    d2 = "D2"
    d3 = "D3"
    nested_small = "NestedSmall"
    default = "Default"


class AccessControlEntryAction(str, Enum):

    permit = "Permit"
    deny = "Deny"


class OperationStatus(str, Enum):

    in_progress = "InProgress"
    failed = "Failed"
    succeeded = "Succeeded"
    timed_out = "TimedOut"
    created = "Created"


class IssueType(str, Enum):

    service_incident = "ServiceIncident"
    app_deployment = "AppDeployment"
    app_crash = "AppCrash"
    runtime_issue_detected = "RuntimeIssueDetected"
    ase_deployment = "AseDeployment"
    user_issue = "UserIssue"
    platform_issue = "PlatformIssue"
    other = "Other"


class SolutionType(str, Enum):

    quick_solution = "QuickSolution"
    deep_investigation = "DeepInvestigation"
    best_practices = "BestPractices"


class RenderingType(str, Enum):

    no_graph = "NoGraph"
    table = "Table"
    time_series = "TimeSeries"
    time_series_per_instance = "TimeSeriesPerInstance"


class ResourceScopeType(str, Enum):

    server_farm = "ServerFarm"
    subscription = "Subscription"
    web_site = "WebSite"


class NotificationLevel(str, Enum):

    critical = "Critical"
    warning = "Warning"
    information = "Information"
    non_urgent_suggestion = "NonUrgentSuggestion"


class Channels(str, Enum):

    notification = "Notification"
    api = "Api"
    email = "Email"
    webhook = "Webhook"
    all = "All"


class AppServicePlanRestrictions(str, Enum):

    none = "None"
    free = "Free"
    shared = "Shared"
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class InAvailabilityReasonType(str, Enum):

    invalid = "Invalid"
    already_exists = "AlreadyExists"


class CheckNameResourceTypes(str, Enum):

    site = "Site"
    slot = "Slot"
    hosting_environment = "HostingEnvironment"
    publishing_user = "PublishingUser"
    microsoft_websites = "Microsoft.Web/sites"
    microsoft_websitesslots = "Microsoft.Web/sites/slots"
    microsoft_webhosting_environments = "Microsoft.Web/hostingEnvironments"
    microsoft_webpublishing_users = "Microsoft.Web/publishingUsers"


class ValidateResourceTypes(str, Enum):

    server_farm = "ServerFarm"
    site = "Site"


class ResolveStatus(str, Enum):

    initialized = "Initialized"
    resolved = "Resolved"
    invalid_syntax = "InvalidSyntax"
    msi_not_enabled = "MSINotEnabled"
    vault_not_found = "VaultNotFound"
    secret_not_found = "SecretNotFound"
    secret_version_not_found = "SecretVersionNotFound"
    access_to_key_vault_denied = "AccessToKeyVaultDenied"
    other_reasons = "OtherReasons"


class ConfigReferenceSource(str, Enum):

    key_vault = "KeyVault"


class ConfigReferenceLocation(str, Enum):

    application_setting = "ApplicationSetting"


class LogLevel(str, Enum):

    off = "Off"
    verbose = "Verbose"
    information = "Information"
    warning = "Warning"
    error = "Error"


class BackupItemStatus(str, Enum):

    in_progress = "InProgress"
    failed = "Failed"
    succeeded = "Succeeded"
    timed_out = "TimedOut"
    created = "Created"
    skipped = "Skipped"
    partially_succeeded = "PartiallySucceeded"
    delete_in_progress = "DeleteInProgress"
    delete_failed = "DeleteFailed"
    deleted = "Deleted"


class DatabaseType(str, Enum):

    sql_azure = "SqlAzure"
    my_sql = "MySql"
    local_my_sql = "LocalMySql"
    postgre_sql = "PostgreSql"


class FrequencyUnit(str, Enum):

    day = "Day"
    hour = "Hour"


class ContinuousWebJobStatus(str, Enum):

    initializing = "Initializing"
    starting = "Starting"
    running = "Running"
    pending_restart = "PendingRestart"
    stopped = "Stopped"


class WebJobType(str, Enum):

    continuous = "Continuous"
    triggered = "Triggered"


class PublishingProfileFormat(str, Enum):

    file_zilla3 = "FileZilla3"
    web_deploy = "WebDeploy"
    ftp = "Ftp"


class DnsVerificationTestResult(str, Enum):

    passed = "Passed"
    failed = "Failed"
    skipped = "Skipped"


class MSDeployLogEntryType(str, Enum):

    message = "Message"
    warning = "Warning"
    error = "Error"


class MSDeployProvisioningState(str, Enum):

    accepted = "accepted"
    running = "running"
    succeeded = "succeeded"
    failed = "failed"
    canceled = "canceled"


class MySqlMigrationType(str, Enum):

    local_to_remote = "LocalToRemote"
    remote_to_local = "RemoteToLocal"


class PublicCertificateLocation(str, Enum):

    current_user_my = "CurrentUserMy"
    local_machine_my = "LocalMachineMy"
    unknown = "Unknown"


class BackupRestoreOperationType(str, Enum):

    default = "Default"
    clone = "Clone"
    relocation = "Relocation"
    snapshot = "Snapshot"
    cloud_fs = "CloudFS"


class UnauthenticatedClientAction(str, Enum):

    redirect_to_login_page = "RedirectToLoginPage"
    allow_anonymous = "AllowAnonymous"


class BuiltInAuthenticationProvider(str, Enum):

    azure_active_directory = "AzureActiveDirectory"
    facebook = "Facebook"
    google = "Google"
    microsoft_account = "MicrosoftAccount"
    twitter = "Twitter"


class CloneAbilityResult(str, Enum):

    cloneable = "Cloneable"
    partially_cloneable = "PartiallyCloneable"
    not_cloneable = "NotCloneable"


class SiteExtensionType(str, Enum):

    gallery = "Gallery"
    web_root = "WebRoot"


class TriggeredWebJobStatus(str, Enum):

    success = "Success"
    failed = "Failed"
    error = "Error"


class SiteRuntimeState(str, Enum):

    ready = "READY"
    stopped = "STOPPED"
    unknown = "UNKNOWN"


class BuildStatus(str, Enum):

    waiting_for_deployment = "WaitingForDeployment"
    uploading = "Uploading"
    deploying = "Deploying"
    ready = "Ready"
    failed = "Failed"
    deleting = "Deleting"
    detached = "Detached"


class TriggerTypes(str, Enum):

    http_trigger = "HttpTrigger"
    unknown = "Unknown"


class K8SEProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    waiting = "Waiting"
    initialization_in_progress = "InitializationInProgress"
    arm_deployment_in_progress = "ARMDeploymentInProgress"
    arm_deployment_finished = "ARMDeploymentFinished"
    infrastructure_setup_in_progress = "InfrastructureSetupInProgress"
    infrastructure_setup_complete = "InfrastructureSetupComplete"
    scheduled_for_delete = "ScheduledForDelete"
    deletion_in_progress = "DeletionInProgress"
    upgrade_requested = "UpgradeRequested"
    upgrade_failed = "UpgradeFailed"
    initialization_failed = "InitializationFailed"


class K8SENetworkPlugin(str, Enum):

    kubenet = "kubenet"
    azure = "azure"


class SkuName(str, Enum):

    free = "Free"
    shared = "Shared"
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"
    dynamic = "Dynamic"
    isolated = "Isolated"
    premium_v2 = "PremiumV2"
    elastic_premium = "ElasticPremium"
    elastic_isolated = "ElasticIsolated"
